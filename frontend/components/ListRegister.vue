<template>
  <b-table :data="persons" paginated pagination-rounded per-page="5">
    <!--<b-field>
        <input
          v-model="nameInput"
          class="mr-3 input is-info"
          placeholder="Nome do técnico"
        />
        <div class="select is-info">
          <b-select v-model="selected" placeholder="Selecione uma stack">
            <option
              v-for="option in stacks"
              :key="option.id"
              :value="option.name"
            >
              {{ option.name }}
            </option>
          </b-select>
        </div>
        <b-button
          class="ml-5"
          type="is-blue"
          icon-left="bi bi-search"
          @click="search(selected, nameInput)"
        ></b-button>
      </b-field>  -->
    <template v-for="column in columns">
      <b-table-column :key="column.id" :label="column.label" v-bind="column">
        <template #default="props">
          <span v-if="column.field == 'actions'">
            <div class="buttons">
              <b-button
                class="border-0"
                type="is-danger"
                outlined
                icon-left="delete"
                @click="confirmRemove(props.row)"
              ></b-button>
              <b-button
                class="border-0"
                type="is-blue"
                outlined
                icon-left="pencil"
                @click="editar(props.row)"
              ></b-button>
            </div>
          </span>
          <span v-if="column.field == 'created_at'">
            {{ new Date(props.row[column.field]).toLocaleDateString() }} -
            {{ new Date(props.row[column.field]).toLocaleTimeString() }}
          </span>
          <span v-else>
            {{ props.row[column.field] }}
          </span>
        </template>
      </b-table-column>
    </template>
  </b-table>
</template>

<script>
export default {
  data() {
    return {
      selected: '',
      names: [],
      nameInput: '',
      persons: [],
      stacks: [],
      columns: [
        {
          field: 'id',
          label: 'Código',
        },
        {
          field: 'name',
          label: 'Nome',
          searchable: true,
        },
        {
          field: 'cpf',
          label: 'CPF',
        },
        {
          field: 'email',
          label: 'Email',
        },
        {
          field: 'stacks',
          label: 'Stacks',
          searchable: true,
          visible: true,
          width: '40',
        },
        {
          field: 'created_at',
          label: 'Criado em',
        },
        {
          field: 'actions',
          label: 'Ações',
        },
      ],
    }
  },
  async fetch() {
    this.persons = await this.$axios.$get('/api/persons')
    this.stacks = await this.$axios.$get('/api/stacks')
  },
  methods: {
    confirmRemove(person) {
      this.$buefy.dialog.confirm({
        title: 'Deletar Cadastro?',
        message: 'Tem certeza que deseja <b>deletar</b> esse cadastro?',
        confirmText: 'Delete',
        cancelText: 'Cancel',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(person),
      })
    },
    async remove(person) {
      person.deleted_at = new Date().toDateString()
      /* Deveria guardar as informações em um arquivo? */
      const url = `/api/persons/${person.id}`
      try {
        await this.$axios.$delete(url)
        this.$toasted.global.defaultSuccess({
          msg: 'Cadastro removido com sucesso',
        })
        this.$fetch()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.date[item])
        }
      }
    },
    editar(person) {
      this.$router.push({
        name: `editRegister`,
        params: { person },
      })
    },
    /*     search(selected, nameInput) {
      this.names = this.persons.filter(
        (person) => person.stacks === selected || person.name === nameInput
      ) tem que filtrar as stacks
    }, */
  },
}
</script>

<style>
.table {
  border: #b9b9b9 solid 0.2px;
}
</style>

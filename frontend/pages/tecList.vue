<template>
  <section>
    <div class="m-5 table d-flex flex-column rounded">
      <b-table :data="persons">
        <b-field>
          <input class="mr-3 input" placeholder="Nome do técnico" />
          <b-select placeholder="Selecione uma stack">
            <option
              v-for="option in columns"
              :key="option.id"
              :value="option.id"
            >
              {{ option.name }}
            </option>
          </b-select>
          <b-button
            class="ml-5"
            type="is-blue"
            icon-left="bi bi-search"
            @click="oi"
          ></b-button>
        </b-field>
        <template v-for="column in columns">
          <b-table-column :key="column.id" :label="column.label">
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
                    @click="oi"
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
    </div>
    {{ persons }}
  </section>
</template>

<script>
// import { mapState } from 'vuex'
export default {
  data() {
    return {
      persons: [],
      columns: [
        {
          field: 'id',
          label: 'Código',
          width: '100',
        },
        {
          field: 'name',
          label: 'Nome',
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
  },
  /*   computed: {
    ...mapState('person', ['persons']),
  }, */
  methods: {
    confirmRemove(person) {
      this.$buefy.dialog.confirm({
        title: 'Deletar Cadastrp?',
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
    async edit(person) {},
  },
}
</script>

<style>
.table {
  width: 90%;
  background-color: #e5e5e5;
  border: #b9b9b9 solid 0.2px;
}
</style>

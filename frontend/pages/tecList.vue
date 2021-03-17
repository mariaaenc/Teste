<template>
  <section>
    <div class="m-5 table d-flex flex-column rounded">
      <b-table :data="persons">
        <b-field>
          <b-input placeholder="Nome do técnico"></b-input>
          <b-select placeholder="Selecione uma stack">
            <option value="1">Option 1</option>
            <option value="2">Option 2</option>
          </b-select>
          <b-button
            type="is-blue"
            icon-left="card-search"
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
              <span v-else>
                {{ props.row[column.field] }}
              </span>
            </template>
          </b-table-column>
        </template>
      </b-table>
    </div>
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
          field: 'date_birth',
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

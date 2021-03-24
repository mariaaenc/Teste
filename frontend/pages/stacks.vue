<template>
  <div class="box column mx-5 mt-3 p-3 color">
    <form @submit.prevent="submit">
      <input id="stack-id" v-model="stack.id" type="hidden" />
      <p>Registro e Edição de Stacks</p>
      <hr />
      <b-field>
        <input
          v-model="stack.name"
          class="input is-info mr-4"
          type="text"
          placeholder="Digite uma Stack"
        />
        <b-button type="is-success" icon-left="check" native-type="submit">
          Salvar
        </b-button>
      </b-field>
    </form>
    <p class="pt-3">Lista</p>
    <hr />
    <b-table :data="stacks">
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
                  @click="loadStack(props.row)"
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
</template>

<script>
// import { mapActions } from 'vuex'
export default {
  props: {
    value: {
      type: Object,
      default() {
        return {}
      },
    },
  },
  data() {
    return {
      stack: {},
      original: {},
      columns: [
        {
          field: 'id',
          label: 'Código',
        },
        {
          field: 'name',
          label: 'Nome',
        },
        {
          field: 'actions',
          label: 'Ações',
        },
      ],
      stacks: [],
    }
  },
  async fetch() {
    this.stacks = await this.$axios.$get('/api/stacks')
  },
  watch: {
    value(newValue) {
      this.original = { ...newValue }
      this.stack = newValue
    },
    stack(newValue) {
      this.$emit('input', newValue)
    },
  },
  created() {
    if (this.value) {
      this.original = { ...this.value }
      this.stack = this.value
    }
  },
  methods: {
    // ...mapActions('stacks', ['getStacks']),
    async submit() {
      const method = this.stack.id ? 'put' : 'post'
      const id = this.stack.id ? `/${this.stack.id}` : ''
      const url = `/api/stacks${id}/`
      try {
        await this.$axios[method](url, this.stack)
        this.$toasted.global.defaultSuccess({
          msg: 'Operação realizada com sucesso',
        })
        // this.getStacks()
        this.reset()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    },
    reset() {
      this.stack = {}
    },
    confirmRemove(stack) {
      this.$buefy.dialog.confirm({
        title: 'Deletar Stack?',
        message: 'Tem certeza que deseja <b>deletar</b> essa stack?',
        confirmText: 'Delete',
        cancelText: 'Cancel',
        type: 'is-danger',
        hasIcon: true,
        onConfirm: () => this.remove(stack),
      })
    },
    async remove(stack) {
      const id = stack.id
      const url = `/api/stacks/${id}`
      try {
        await this.$axios.delete(url)
        this.$toasted.global.defaultSuccess()
        // this.getStacks()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    },
    loadStack(stack) {
      this.stack = {
        id: stack.id,
        name: stack.name,
      }
    },
  },
}
</script>

<style>
.color {
  background-color: #e5e5e5;
  border: #b9b9b9 solid 0.2px;
}
</style>

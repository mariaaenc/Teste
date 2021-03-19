<template>
  <section>
    <form
      class="mx-5 mt-3 p-3 d-flex flex-column rounded form"
      @submit.prevent="submit"
    >
      <input id="person-id" v-model="person.id" type="hidden" />
      <div class="p-1">
        <p>Formulário do Técnico</p>
        <hr />
        <b-field>
          <input
            v-model="person.name"
            class="input is-info"
            type="text"
            placeholder="Nome do Técnico"
          />
        </b-field>

        <b-field>
          <input
            v-model="person.cpf"
            class="input is-info"
            type="text"
            placeholder="CPF do Técnico"
          />
        </b-field>

        <b-field>
          <input
            v-model="person.email"
            class="input is-info"
            placeholder="Email do Técnico"
            type="email"
          />
        </b-field>

        <b-field>
          <input
            v-model="person.date_birth"
            class="input is-info"
            placeholder="Data de Nascimento"
            type="date"
          />
        </b-field>

        <b-field>
          <input
            v-model="person.address"
            class="input is-info"
            placeholder="Endereço do Técnico"
            type="text"
          />
        </b-field>

        <b-field>
          <input
            v-model="person.stacks"
            class="input is-info"
            placeholder="Stacks"
            type="text"
          />
        </b-field>
        <hr />
        <b-field>
          <router-link to="tecList" class="button is-primary mr-2 link">
            Voltar
          </router-link>
          <b-button native-type="submit" type="is-success"> Salvar </b-button>
        </b-field>
      </div>
    </form>
  </section>
</template>

<script>
export default {
  asyncData({ params }) {
    return {
      person: params.person,
    }
  },
  data() {
    return {}
  },
  methods: {
    async submit() {
      const url = `/api/persons/${this.person.id}/`
      this.person.update_at = new Date().toDateString()
      try {
        await this.$axios.patch(url, this.person)
        this.$toasted.global.defaultSuccess()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    },
  },
}
</script>

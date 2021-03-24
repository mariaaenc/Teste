<template>
  <form class="mx-5 mt-3 p-3 rounded form" @submit.prevent="submit">
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
      <b-field class="box">
        <div v-for="stack in stacks" :key="stack.id">
          <b-checkbox v-model="checkboxGroup" :native-value="stack.name">
            {{ stack.name }}
          </b-checkbox>
        </div>
      </b-field>
      <hr />
      <b-field class="d-flex justify-content-end">
        <b-button native-type="submit" type="is-success"> Salvar </b-button>
      </b-field>
    </div>
    <!-- <div>Selecionados: {{ person }}</div> -->
  </form>
</template>

<script>
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
      person: { stacks: [] },
      stacks: [],
      checkboxGroup: [],
    }
  },
  async fetch() {
    this.stacks = await this.$axios.$get('/api/stacks')
  },
  methods: {
    async submit() {
      try {
        this.person.stacks = []
        this.checkboxGroup.forEach((element) => {
          this.person.stacks.push({
            stack: this.stacks.filter((stack) => stack.name === element)[0].id,
          })
        })
        await this.$axios.$post('/api/persons/', this.person)
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

<style>
p {
  font-weight: bold;
  color: #244873;
  font-size: 20px;
}
.form {
  background-color: #e5e5e5;
  border: #b9b9b9 solid 0.2px;
}
</style>

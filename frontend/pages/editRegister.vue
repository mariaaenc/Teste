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

        <!--<div class="d-flex justify-content-end">
          <b-button
            type="is-primary"
            icon-left="plus-box-multiple"
            size="is-small"
            @click="add()"
          >
            Nova Stack
          </b-button>
        </div> -->
        <!-- <b-field>
          <b-tag
            v-for="stack in person.stacks"
            :key="stack.id"
            class="is-primary ml-1"
            placeholder="Stacks"
          >
            {{ stack.stack_name }}
          </b-tag>
        </b-field> -->
        <b-field class="box">
          <div v-for="stack in stacks" :key="stack.id">
            <b-checkbox v-model="checkboxGroup" :native-value="stack.name">
              {{ stack.name }}
            </b-checkbox>
          </div>
        </b-field>
        <hr />
        <div class="d-flex justify-content-end">
          <router-link to="tecList" class="button is-primary mr-2 link">
            Voltar
          </router-link>
          <b-button native-type="submit" type="is-success"> Salvar </b-button>
        </div>
      </div>
    </form>
    <!-- {{ checkboxGroup }} -->
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
    return {
      stacks: [],
      checkboxGroup: [],
    }
  },
  async fetch() {
    this.stacks = await this.$axios.$get('/api/stacks')
    this.loadCheck()
  },
  methods: {
    loadCheck() {
      this.person.stacks.forEach((stack) => {
        this.checkboxGroup.push(stack.stack_name)
      })
    },
    async submit() {
      const url = `/api/persons/${this.person.id}/`
      try {
        this.person.stacks = []
        this.checkboxGroup.forEach((element) => {
          this.person.stacks.push({
            stack: this.stacks.filter((stack) => stack.name === element)[0].id,
          })
        })
        this.person.updated_at = new Date().toISOString()
        await this.$axios.put(url, this.person)
        this.$toasted.global.defaultSuccess()
      } catch (err) {
        for (const item in err.response.data) {
          this.$toast.error(item + ': ' + err.response.data[item])
        }
      }
    },
    /*    add() {
      this.$router.push({
        name: `stacks`,
      })
    }, */
  },
}
</script>

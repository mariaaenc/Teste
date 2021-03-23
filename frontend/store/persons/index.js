export const state = () => ({
  persons: [],
})

export const mutations = {
  loadPersons(state, persons) {
    state.persons = persons
  },
}

export const actions = {
  async getPersons({ commit }) {
    const persons = await this.$axios.$get('/api/persons')
    commit('loadPersons', persons)
  },
}

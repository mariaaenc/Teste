export const state = () => ({
  persons: [
    {
      id: 1,
      name: 'Maria',
      cpf: '12213434913',
      email: 'maria@maria.com',
      date_birth: '2016-10-15 13:43:27',
      actions: 'actions',
    },
    {
      id: 2,
      name: 'John',
      cpf: '12213434913',
      email: 'maria@maria.com',
      date_birth: '2016-12-15 06:00:53',
      actions: 'actions',
    },
    {
      id: 3,
      name: 'Tina',
      cpf: '12213434913',
      email: 'maria@maria.com',
      date_birth: '2016-04-26 06:26:28',
      actions: 'actions',
    },
    {
      id: 4,
      name: 'Clarence',
      cpf: '12213434913',
      email: 'maria@maria.com',
      date_birth: '2016-04-10 10:28:46',
      actions: 'actions',
    },
    {
      id: 5,
      name: 'Anne',
      cpf: '12213434913',
      email: 'maria@maria.com',
      date_birth: '2016-12-06 14:38:38',
      actions: 'actions',
    },
  ],
})

/* export const mutations = {
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

export const getters = {
  listPersons: (state) => {
    return state.persons
  },
} */

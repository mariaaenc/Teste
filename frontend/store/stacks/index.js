export const state = () => ({
  stacks: [],
})

export const mutations = {
  loadStacks(state, stacks) {
    state.stacks = stacks
  },
}

export const actions = {
  async getStacks({ commit }) {
    const stacks = await this.$axios.$get('/api/stacks')
    commit('loadStacks', stacks)
  },
}

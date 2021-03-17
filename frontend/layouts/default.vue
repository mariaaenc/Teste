<template>
  <div>
    <nav class="pl-6 navbar is-blue size">
      <div class="navbar-brand">Teste BoxTI</div>
    </nav>
    <section class="columns">
      <aside class="column is-2 section nav">
        <ul class="menu-list">
          <span v-if="loggedIn">
            <li v-for="(item, key) of authenticatedItems" :key="key">
              <nuxt-link :to="item.to" exact-active-class="is-active">
                <b-icon :icon="item.icon" />
                {{ item.title }}
              </nuxt-link>
            </li>
          </span>
        </ul>
      </aside>
      <div class="container column is-10">
        <nuxt />
      </div>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  data() {
    return {
      authenticatedItems: [
        {
          title: 'Lista de Técnicos',
          icon: 'format-list-bulleted',
          to: { name: 'tecList' },
        },
        {
          title: 'Cadastro Téc...',
          icon: 'account-plus',
          to: { name: 'tecRegister' },
        },
        {
          title: 'Sair',
          icon: 'logout',
          to: { name: 'logout' },
        },
      ],
    }
  },
  computed: {
    ...mapState('auth', ['loggedIn']),
  },
}
</script>

<style></style>

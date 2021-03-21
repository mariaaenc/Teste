<template>
  <div>
    <nav
      class="navbar pl-6 is-blue size"
      role="navigation"
      aria-label="main navigation"
    >
      <div class="navbar-brand">Teste BoxTI</div>
    </nav>

    <section class="main-content columns tm">
      <aside class="column is-2 section nav pt-5 pl-5">
        <ul class="menu-list p-0">
          <li v-for="(item, key) of globalItems" :key="key">
            <nuxt-link
              :to="item.to"
              exact-active-class="is-active"
              class="link"
            >
              <b-icon :icon="item.icon" />
              {{ item.title }}
            </nuxt-link>
          </li>
          <span v-if="loggedIn">
            <li v-for="(item, key) of authenticatedItems" :key="key">
              <nuxt-link
                :to="item.to"
                exact-active-class="is-active"
                class="link"
              >
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
      globalItems: [
        {
          title: 'Home',
          icon: 'home',
          to: { name: 'index' },
        },
      ],
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

<style>
.tm {
  min-height: calc(100vh - 52px + 0.75rem);
}
.size {
  height: 10px;
  font-weight: bold;
}

.nav {
  background-color: #2f3c4a;
}
</style>

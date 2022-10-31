<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"><strong>Monster Quiz</strong></router-link>
      </div>

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <template v-if="$store.state.isAuthenticated">
                <router-link to="/my-account" class="button is-light">My account</router-link>
              </template>

              <template v-else>
                <router-link to="/log-in" class="button is-light">Log in</router-link>
                <router-link to="/sign-up" class="button is-light">Sign Up</router-link>
              </template>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view/>
    </section>

    <footer class="footer">
      <p class="has-text-centered">Copyright (c) 2022</p>
      <p class="has-text-centered">Team: West Coast App Monsters</p>
      <p class="has-text-centered">Team Member: Gan Li, Ruosha Pang, Zhaowei Si</p>
    </footer>
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue'
export default {
  components: {NavBar}
}
</script>

<style lang="scss">
@import '../node_modules/bulma';
.form-signin {
  max-width: 330px;
  padding: 15px;
}
.form-signin .form-floating:focus-within {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>

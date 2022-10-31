<template>
    <div class="container">
      <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li><router-link to="/" class="nav-link px-2 link-dark">Monster Quiz</router-link></li>
        </ul>

        <div class="text-end">
          <router-link to ="/login" class="btn btn-outline-primary me-2">Login</router-link>
          <router-link to ="/signup" class="btn btn-primary">Sign-up</router-link>
        </div>
      </div>
    </div>
</template>

<script>

export default {
  name: 'NavBar',
}
</script>

<style scoped>

</style>

<template>
  <main class="form-signin w-100 m-auto">
  <form @submit.prevent="submit">
    <h1 class="h3 mb-3 fw-normal">Welcome to Sign Up</h1>

    <div class="form-floating">
      <input v-model="data.email" type="email" class="form-control" placeholder="name@example.com">
      <label>Email address</label>
    </div>
    <div class="form-floating">
      <input v-model="data.password" type="password" class="form-control" placeholder="Password">
      <label>Password</label>
    </div>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign Up</button>
    <p></p>
    Or <router-link to="/login">click here</router-link> to log in!
  </form>
  </main>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';

export default {
  name: 'SignUp',
  setup(){
    const data = reactive({
      email: '',
      password: ''
    });

    const router = useRouter();

    const submit = async () => {
      await axios.post('http://localhost:8000/api/signup', data);

      await router.push('/login');
    }

    return {
      data,
      submit 
    }
  }
}
</script>
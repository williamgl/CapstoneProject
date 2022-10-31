<template>
  <main class="form-signin w-100 m-auto">
  <form @submit.prevent = "submit">
    <h1 class="h3 mb-3 fw-normal">Log In</h1>

    <div class="form-floating">
      <input v-model="data.email" type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
      <label for="floatingInput">Email Address</label>
    </div>
    <div class="form-floating">
      <input v-model="data.password" type="password" class="form-control" id="floatingPassword" placeholder="Password">
      <label for="floatingPassword">Password</label>
    </div>

    <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
    <p></p>
    Or <router-link to="/signup">click here</router-link> to sign up!
  </form>
  </main>
</template>

<script>
import { reactive } from 'vue';
import axios from 'axios';
import {useRouter} from 'vue-router';
export default {
  name: 'LogIn',
  setup() {
    const data = reactive({
      email: '',
      password: ''
    });
    const router = useRouter ();
    const submit = async () =>{
      const response = await axios.post('http://localhost:8000/api/login', data, {
        withCredentials: true
      });
      //https://axios-http.com/docs/config_defaults
      //https://www.tabnine.com/code/javascript/functions/axios/AxiosRequestConfig/headers
      axios.defaults.headers.common['Authorization'] = `Bearer ${response.data.token}`;
      await router.push('/');
    }

    return {
      data, submit
    }
  }
}
</script>
<template>

  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Monster Quiz
            </p>
            <p class="subtitle">
              <h3>Get Answers with Quizzes</h3>
              <h4>Be the Person with Great Concepts</h4>
            </p>
        </div>
    </section>

    <div class="hero is-medium is-white mb-6">
      <router-link to="/log-in" class="button is-dark">Log in</router-link>
      <p class="hero is-medium is-light mb-6"></p>
      <router-link to="/sign-up" class="button is-dark">Sign Up</router-link>
    </div>

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Some Latest Questions</h2>
      </div>

      <div class="column is-3"
        v-for="question in latestQuestions"
        v-bind:key="question.id">

        <div class="box">

          <h3 class="is-size-4">{{ question.name }}</h3>
          <p class="is-size-6 has-text-grey">Price: ${{ question.score }}</p>

          <router-link
            v-bind:to="question.get_absolute_url"
            class="button is-dark mt-4">
            View Detail
          </router-link>

        </div>
      </div>

      <div>
      <QuestionBox
       v-for="question in latestQuestions"
       v-bind:key="question.id"
       v-bind:question="question"
      />
      </div>

    </div>
  </div>

</template>


<script>
import axios from 'axios'
import QuestionBox from '@/components/QuestionBox'
export default {
  name: 'HomePage',
  data() {
    return {
      latestQuestions: []
    }
  },
  components: {
    QuestionBox
  },
  mounted() {
    this.getLatestQuestions()
    document.title = 'Home | Monster Quiz'
  },
  methods: {
    async getLatestQuestions() {
      await axios
        .get('/api/v1/latest-questions/')
        .then(response => {
          this.latestQuestions = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
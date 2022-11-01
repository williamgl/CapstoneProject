<template>
    <div class="page-question">
        <div class="columns is-multiline">
            <div class="column is-9">

                <h1 class="title">{{ question.name }}</h1>

                <p>{{ question.description }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Information</h2>

                <p><strong>Score: </strong>{{ question.score }}</p>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Question',
    data() {
        return {
            question: {}
        }
    },
    mounted() {
        this.getQuestion()
    },
    methods: {
        async getQuestion() {
            const quiz_slug = this.$route.params.quiz_slug
            const question_slug = this.$route.params.question_slug

            await axios
                .get(`/api/v1/questions/${quiz_slug}/${question_slug}`)
                .then(response => {
                    this.question = response.data
                    document.title = 'Monster Quiz'
                })
                .catch(error => {
                    console.log(error)
                })
        },
    }
}
</script>
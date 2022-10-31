<template>
    <div class="column is-3">
        <div class="box">

            <h3 class="is-size-4">{{ question.name }}</h3>
            <p class="is-size-6 has-text-grey">Score: {{ question.score }}</p>

            <router-link
             v-bind:to="question.get_absolute_url"
             class="button is-dark mt-4">
             View details
            </router-link>

        </div>
    </div>
</template>

<script>
export default {
    name: 'QuestionBox',
    props: {
        question: Object
    }
}
</script>
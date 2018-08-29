Vue.component('records-list', {
    data() {
        return {
            records: []
        }
    },
    mounted() {
        axios.get('/repo/records/')
            .then(response => this.records = response.data)
            .catch(response => console.log('error: ' + response))
    },
});

const app = new Vue({
    delimiters: ['((', '))'],
    el: '#app',
});
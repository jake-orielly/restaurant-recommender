<template>
  <div>
    <p>
      Hi
    </p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'ReccomenderWindow',
  mounted () {
    axios
      .get('https://api.coindesk.com/v1/bpi/currentprice.json')
      .then(response => (this.info = response))
  }
}
</script>

<style scoped>

</style>

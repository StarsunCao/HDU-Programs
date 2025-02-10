<template>
  <div class="navbar">
    <div class="right-menu">
          <el-button type="success" round @click="logout">Logout</el-button>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: "Navbar",
  data() {
    return {

    };
  },
  
  computed: {
    ...mapGetters([
      'sidebar',
      'avatar'
    ])
  },
  methods: {
    
    logout() {
      localStorage.removeItem('hasLogin')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  },

}
</script>

<style lang="scss" scoped>

.navbar {
  height: 50px;
  overflow: hidden;
  position: relative;
  background: #fff;
  box-shadow: 0 1px 4px rgba(0, 21, 41, 0.08);
  .right-menu {
    float: right;
    height: 100%;
    line-height: 50px;
    margin-right: 20px;

    &:focus {
      outline: none;
    }

    
  }
}
</style>

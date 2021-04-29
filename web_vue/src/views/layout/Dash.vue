<template>
    <b-container fluid >
        <Header></Header>
            <router-view/>
    </b-container>
</template>


<script>

    import Header from "./Header";
    export default {
        name: "Dash",
        components:{
            Header
        }
    }
</script>

<style scoped>
.container-fluid{
    padding-left: 0;
    padding-right: 0;
    margin-left: 0;
    margin-right: 0;
}
.row{
 }
</style>
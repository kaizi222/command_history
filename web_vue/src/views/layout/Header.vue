<template>
            <div>
                <b-navbar toggleable="lg" type="dark" variant="info">
                    <b-navbar-brand href="#">NavBar</b-navbar-brand>
                    <b-navbar-brand href="#"><b-link to="/history" router-tag="b-navbar-brand">时间记录</b-link></b-navbar-brand>
                    <b-navbar-brand href="#"><b-link to="/lump" router-tag="b-navbar-brand">命令记录</b-link></b-navbar-brand>
                    <b-navbar-brand href="#"><b-link to="/share" router-tag="b-navbar-brand">分享库</b-link></b-navbar-brand>
                    <b-navbar-brand href="#"><b-link to="" router-tag="b-navbar-brand">智库</b-link></b-navbar-brand>
                    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
                    <b-collapse id="nav-collapse" is-nav>
                        <!-- Right aligned nav items -->
                        <!--<b-navbar-nav class="ml-auto">
                            <b-nav-item-dropdown right>
                                &lt;!&ndash; Using 'button-content' slot &ndash;&gt;
                                <template #button-content>
                                    <em><b-avatar variant="info" src="https://placekitten.com/300/300"></b-avatar></em>
                                </template>
                                <b-dropdown-item href="#">Profile</b-dropdown-item>
                                <b-dropdown-item href="#">Sign Out</b-dropdown-item>
                            </b-nav-item-dropdown>
                        </b-navbar-nav>-->
                    </b-collapse>
                </b-navbar>
            </div>
</template>

<script>
    export default {
        name: "Header"
    }
</script>

<style scoped>

</style>
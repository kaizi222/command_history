<template>
    <b-row>
        <b-col align-self="stretch" align-h="start" cols="2">
            <div>
                <b-nav vertical class="w-20" align="center">
                    <div class="accordion" role="tablist">
                        <b-card no-body class="mb-1">
                            <b-card-header header-tag="header"   class="p-1" role="tab" variant="danger">
                                <b-button block v-b-toggle.accordion-1 variant="info">Accordion 1</b-button>
                            </b-card-header>
                            <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                                <b-card-body>
                                    <div>
                                        <b-button-group vertical>
                                            <b-button><router-link to="/">Home</router-link></b-button>
                                            <b-button><router-link to="/about">About</router-link></b-button>
                                            <b-button><router-link to="/kline">kline</router-link></b-button>
                                        </b-button-group>
                                    </div>
                                </b-card-body>
                            </b-collapse>
                        </b-card>

                        <b-card no-body class="mb-1">
                            <b-card-header header-tag="header" class="p-1" role="tab">
                                <b-button block v-b-toggle.accordion-2 variant="info">Accordion 2</b-button>
                            </b-card-header>
                            <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                                <b-card-body>
                                    <b-card-text></b-card-text>
                                </b-card-body>
                            </b-collapse>
                        </b-card>

                        <b-card no-body class="mb-1">
                            <b-card-header header-tag="header" class="p-1" role="tab">
                                <b-button block v-b-toggle.accordion-3 variant="info">Accordion 3</b-button>
                            </b-card-header>
                            <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                                <b-card-body>
                                    <b-card-text></b-card-text>
                                </b-card-body>
                            </b-collapse>
                        </b-card>
                    </div>


                </b-nav>
            </div>
        </b-col>
        <b-col>
            <router-view/>
        </b-col>
    </b-row>
</template>

<script>
    export default {
        name: "Content"
    }
</script>

<style scoped>

</style>
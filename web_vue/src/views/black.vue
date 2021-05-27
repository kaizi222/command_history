<template>
    <b-col md="8" offset-md="2">
        <!--<div>
            <b-form-select v-model="selected" :options="options"></b-form-select>
            <b-form-select v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>
            <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
        </div>-->
        <b-row class="mt-3 mb-3">
            <b-col>
                <div>
                    <b-form inline @submit="searchByName">
                        <!--<label class="sr-only" for="inline-form-input-name">Name</label>
                        <b-form-timepicker  locale="en"></b-form-timepicker>
                        <label class="sr-only" for="inline-form-input-username">Username</label>
                        <b-form-timepicker  locale="en"></b-form-timepicker>-->
                        <b-form-input v-model="form.searchName" placeholder="Enter your command"></b-form-input>
                        <b-button type="submit"  variant="primary" >搜索</b-button>
                        <b-button type="submit"  @click="info2($event.target)" >添加</b-button>
                    </b-form>
                </div>
            </b-col>
        </b-row>
<!--        <div>-->
<!--            <b-form inline>-->
<!--                <label class="sr-only" for="inline-form-input-name">Name</label>-->
<!--                <b-form-timepicker  locale="en"></b-form-timepicker>-->

<!--                <label class="sr-only" for="inline-form-input-username">Username</label>-->
<!--                <b-form-timepicker  locale="en"></b-form-timepicker>-->
<!--                <b-form-input v-model="text" placeholder="Enter your name"></b-form-input>-->
<!--                <b-button variant="primary">Save</b-button>-->
<!--            </b-form>-->
<!--        </div>-->

        <b-table hover :items="items" :fields="fields"  :borderless="true" :small="true" >
        </b-table>
        <!-- Info modal -->
        <b-modal :id="infoModal.id" :title="infoModal.title" size="xl" hide-footer>
            <pre>{{ infoModal.content }}</pre>
            <div>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                <b-form-group
                        id="input-group-1"
                        label="命令:"
                        label-for="input-1"
                >
                    <b-form-input
                            id="input-1"
                            type="text"
                            v-model="form.cmd"
                            placeholder="cmd"
                            required
                    ></b-form-input>
                </b-form-group>
                <b-button type="submit" variant="danger">Submit</b-button>
                <pre>{{ infoModal.result }}</pre>
            </b-form>
            </div>
        </b-modal>
    </b-col>
</template>

<script>
    import { formatDate } from '@/directives/time_format'
    export default {
        data() {
            return {
                fields:[
                    {key:'cmd' , label: '时间' },
                    {key:'create_time' , label: '命令' }

                ],
                items: [
                    { time: 40,command:'楷紫国际', description: 'Dickerson'}
                ],
                infoModal: {
                    id: 'info-modal',
                    title: '',
                    content: '',
                    result:'ff'
                },
                form: {
                    code: '',
                    day: '',
                    description: "",
                    cmd: '',
                    grade: '',
                    id:'',
                    searchName:'',
                },
                show: true,
                value: 333,
                text: 'ddd',
                currentPage:1,
                pages :"1"
            }
        },
        created() {
            const _this = this
            this.axios.get('getBlackAll?pages=0&number=3').then(function (resp) {
                _this.items = modify(resp.data)
                console.log(resp.data[0])
                _this.pages = resp.data["count"]*20
            })
        },
        methods:{
            getGoodsList:function () {
                this.axios.get(`buyRemind/getAll/six/${this.currentPage-1}/20`).then(function (resp) {
                    console.log(resp.data["content"])
                })
            },onReset(event) {
                event.preventDefault()
                // Reset our form values
                this.form.description = ''
                // Trick to reset/clear native browser form validation state
                this.show = false
                this.$nextTick(() => {
                    this.show = true
                    this.grade = 1
                })
            },info(item, index, button) {
                this.infoModal.title = `添加描述：`
                this.infoModal.content = `命令：${item.command}\n描述：${item.description}`
                this.form.id = `${item.id}`
                this.form.code = item.code
                this.form.day = item.day
                this.$root.$emit('bv::show::modal', this.infoModal.id, button)
            },info2( button) {
                this.$root.$emit('bv::show::modal', this.infoModal.id, button)
            },onSubmit(event) {
                event.preventDefault()
                const __this = this
                if(this.form.id == 0){
                    this.axios.post(`addBlack`,{
                            cmd:this.form.cmd
                    }).then(function (resp) {
                        if(resp.data == 2){
                            alert("成功")
                            __this.infoModal.result = '添加成功'
                            __this.searchByName()
                            __this.$nextTick(() => {
                                __this.$bvModal.hide('info-modal')
                            })
                        }
                    })
                }else{
                    alert("update")
                    this.axios.post(`update_command`,{
                        id:this.form.id,
                        description:this.form.descriptionadd
                    }).then(function (resp) {
                        alert(resp.data)
                        if(resp.data == 2){
                            this.infoModal.result = "分享成功！"
                        }
                    })
                }

                // alert(JSON.stringify(this.form))

            },searchByName() {
                const _this = this
                this.axios.get('getBlackAll?name='+this.form.searchName).then(function (resp) {
                    _this.items = modify(resp.data)
                })
            },addBlack(){
                this.axios.post(`addBlack`,{
                    id:this.form.id,
                    description:this.form.descriptionadd
                }).then(function (resp) {
                    alert(resp.data)
                    if(resp.data == 2){
                        this.infoModal.result = "分享成功！"
                    }
                })
            }
        },
        filters:{
            formatDate(time) {
                // 秒处理为毫秒
                time = time * 1000
                let date = new Date(time)
                return formatDate(date, 'yyyy-MM-dd hh:mm')
            },
        }

    }
    function modify(items) {
        for(var i = 0 ; i < items.length; i++){
            items[i]['create_time'] = formatDate(items[i]['create_time'], 'yyyy-MM-dd hh:mm')
        }
        return items
    }
</script>

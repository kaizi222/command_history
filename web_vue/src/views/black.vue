<template>
    <b-col md="8" offset-md="2">
        <!--<div>
            <b-form-select v-model="selected" :options="options"></b-form-select>
            <b-form-select v-model="selected" :options="options" size="sm" class="mt-3"></b-form-select>
            <div class="mt-3">Selected: <strong>{{ selected }}</strong></div>
        </div>-->

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
            <template #cell(actions)="row">
                <b-button size="sm" @click="info(row.item, row.index, $event.target)" class="mr-1" variant="outline-primary">
                    添加描述
                </b-button>
                <b-button size="sm" @click="info2(row.item, row.index, $event.target)" class="mr-1" variant="outline-success">
                    分享
                </b-button>
            </template>

        </b-table>

        <!-- Info modal -->
        <b-modal :id="infoModal.id" :title="infoModal.title" size="xl" ok-only>
            <pre>{{ infoModal.content }}</pre>
            <div>
            <b-form @submit="onSubmit" @reset="onReset" v-if="show">
                <b-form-group
                        id="input-group-1"
                        label="添加描述:"
                        label-for="input-1"
                >
                    <b-form-input
                            id="input-1"
                            type="text"
                            v-model="form.descriptionadd"
                            placeholder="描述"
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
    export default {
        data() {
            return {
                fields:[
                    {key:'time' , label: '时间' },
                    {key:'command' , label: '命令' },
                    {key:'description' , label: '描述'},
                    {key:'actions' , label: '描述'}

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
                    descriptionadd: '',
                    grade: '',
                    id:'',
                },
                show: true,
                value: 333,
                text: 'ddd'
            }
        },
        created() {
            const _this = this
            this.axios.get('getAll').then(function (resp) {
                _this.items = modify(resp.data)
                console.log(resp.data[0]['time'])
                _this.pages = resp.data["count"]*20
                console.log( resp.data)
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
            },info2(item, index, button) {
                this.infoModal.title = `分享: `
                this.infoModal.content = `命令：${item.command}\n描述：${item.description}`
                this.form.command = item.command
                this.form.description = item.description
                this.$root.$emit('bv::show::modal', this.infoModal.id, button)
            },onSubmit(event) {
                event.preventDefault()
                const __this = this
                if(this.form.id == 0){
                    this.axios.post(`add_share`,{
                            command:this.form.command,
                        description:this.form.description+this.form.descriptionadd
                    }).then(function (resp) {
                        if(resp.data == 2){
                            alert("进入")
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

            }
        }

    }
    function modify(items) {
         var mycars=new Set()
        var data_array=new Array()
        for(var i = 0 ; i < items.length; i++){
            let date = new Date(items[i]['time']*1000)
            var day = `${date.getFullYear()}-${date.getMonth()+1}-${date.getDate()}`
             if(!mycars.has(day)){
                 mycars.add(day)
                 data_array.push({"time":day,"variant":"primary"});
             }
            items[i]['time'] = `${date.getHours()}:${date.getMinutes()}:${date.getSeconds()} `;
            data_array.push(items[i])
        }
        return data_array
    }
</script>

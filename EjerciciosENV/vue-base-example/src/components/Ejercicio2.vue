<template> 
    <div>
    <h1> Calculadora</h1>
    <div> 
        <input v-model="num1" type="number"/>
        <input v-model="nums2" type="number"/>
    </div>
    <button v-on:click="op(1)"> Suma </button>
    <button v-on:click="op(2)"> Resta </button>
    <button v-on:click="op(3)"> Multiplicacion </button>
    <button v-on:click="op(4)"> Division </button>
    <p> El resultado es {{resultado}}</p>
    </div>
</template>

<script>
/* eslint-disable */
export default {
  name: 'Main',
  data: function(){
    return {
      num1:0,
      num2:0,
      resutado:undefined,
      operacion:""
    }
  },
  methods: { 
    op(operacion){
        this.operacion=operacion;

        const num1=parseFloat(this.num1)
        const num2=parseFloat(this.num2)

        if(this.operacion===1){
            this.resultado= this.num1 + this.num2;
        }else if (this.operacion===2){
            this.resultado = this.num1 - this.num2;
        }else if (this.operacion===3){
            this.resultado = this.num1 * this.num2;
        }else if (this.operacion===4){
            this.resultado = this.num1/ this.num2
        }
        
    }

    }
}

</script>
  


<template>
  <section>
    <div class="m-5 p-2 d-flex flex-column rounded form">
      <b-field>
        <p type="is-blue">Formulário do Técnico</p>
      </b-field>
      <b-field>
        <b-input placeholder="Nome do Técnico"></b-input>
      </b-field>

      <b-field>
        <b-input placeholder="CPF do Técnico"> </b-input>
      </b-field>

      <b-field>
        <b-input placeholder="Email do Técnico" type="email"></b-input>
      </b-field>

      <b-field>
        <b-input placeholder="Data de Nascimento" type="date"></b-input>
      </b-field>

      <b-field>
        <b-input placeholder="Endereço do Técnico" type="text"></b-input>
      </b-field>

      <b-field class="d-flex justify-content-start">
        <b-input type="textarea"> </b-input>
      </b-field>

      <b-field class="d-flex justify-content-end">
        <b-button type="is-success"> Salvar </b-button>
      </b-field>
    </div>
  </section>
</template>

<script>
export default {}
</script>

<style>
.form {
  background-color: #e5e5e5;
}
</style>

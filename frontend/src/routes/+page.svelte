<script>
  let name = $state('');
  let responseMessage = $state('');

  async function fetchGreeting() {
    if (!name) return;
    try {
      const res = await fetch(`http://localhost:8000/api/greet?name=${encodeURIComponent(name)}`);
      const data = await res.json();
      responseMessage = data.message;
    } catch (err) {
      responseMessage = 'Failed to connect to backend server.';
    }
  }
</script>

<main>
  <h1>SvelteKit + Python Backend</h1>

  <div>
    <input 
      type="text" 
      bind:value={name} 
      placeholder="Enter your name" 
    />
    <button onclick={fetchGreeting}>Greet Me</button>
  </div>

  {#if responseMessage}
    <p>{responseMessage}</p>
  {/if}
</main>

<style>
  main {
    font-family: sans-serif;
    max-width: 400px;
    margin: 50px auto;
    text-align: center;
  }
  input, button {
    padding: 8px 12px;
    margin: 5px;
  }
</style>
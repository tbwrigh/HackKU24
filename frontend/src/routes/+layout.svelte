<script lang="ts">
  import "../app.css";
  import { goto, afterNavigate } from '$app/navigation';
  import { page } from '$app/stores';
  import { base } from '$app/paths'
  import { Button } from 'flowbite-svelte';
  import { ArrowLeftOutline } from 'flowbite-svelte-icons';

  let previousPage : string = base ;

  afterNavigate(({from}) => {
     previousPage = from?.url.pathname || previousPage
  });

  console.log("url", $page.url);
</script>

{#if $page.url.pathname != "/"}
  <Button on:click={() => goto(previousPage)} class="z-10 fixed ml-2 mt-2">
    <ArrowLeftOutline class="w-8 h-8" />
  </Button>
{/if}

<header class="fixed w-full flex justify-center place-content-center py-5">
  <a href="/" alt="return to home page" class="z-50 font-extrabold text-xl text-white">Kioku</a>
</header>
<slot></slot>

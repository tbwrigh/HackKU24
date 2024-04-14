<script lang="ts">
  import "../app.css";
  import { goto, afterNavigate } from '$app/navigation';
  import { page } from '$app/stores';
  import { base } from '$app/paths'
  import { Button } from 'flowbite-svelte';
  import { ArrowLeftOutline } from 'flowbite-svelte-icons';

  let parentPage : string = base ;

  afterNavigate(({from}) => {
    parentPage = $page.url.toString().slice(0, $page.url.toString().lastIndexOf('/'));
    if (parentPage.endsWith("/patient")) parentPage = "/";
  });
</script>

{#if $page.url.pathname != "/"}
  <Button on:click={() => goto(parentPage)} class="z-10 fixed ml-2 mt-2">
    <ArrowLeftOutline class="w-8 h-8" />
  </Button>
{/if}

<header class="fixed w-full flex justify-center place-content-center py-5">
  <a href="/" alt="return to home page" class="z-50 font-extrabold text-xl text-white">Kioku</a>
</header>
<slot></slot>

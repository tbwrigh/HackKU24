<script lang="ts">
  import { Button, Heading } from 'flowbite-svelte';
  import type { SelectItem } from './types';

  export let heading: string;
  export let options: SelectItem[];
</script>

<div class="flex w-dvw h-dvh justify-center items-center place-content-center">
  <div class="w-[65ch] flex flex-col gap-4">
    <Heading tag="h1" class="text-4xl text-center text-white">{heading}</Heading>
    {#each options as option}
      <Button href={option.href} size="lg" class="mx-4 hover:ml-8 hover:mr-0 font-bold border-white border-2 hover:border-3 hover:font-extrabold transition-all" pill>{option.label}</Button>
    {/each}
  </div>
</div>

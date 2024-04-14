<script lang="ts">
  import type { PageData } from './$types';
  import type { SelectItem } from '$lib/types';
  import { Button } from 'flowbite-svelte';
  import { CogOutline } from 'flowbite-svelte-icons';
  import Selection from '$lib/selection.svelte';

  export let data: PageData;

  const games = ["Matching", "Flashcards", "Puzzles"];

  let options: SelectOption[] = [];
  games.forEach((game) => {
    const item: SelectOption = {
      href: `/patient/${data.slug}/${game.toLowerCase()}`,
      label: game
    };
    options = [...options, item];
  });
</script>

<Selection heading={`${data.name}'s Profile`} {options} />

<div class="fixed bottom-4 right-4 z-50">
<a href={`/manage/${data.slug}`}>
  <CogOutline class="w-12 h-112 text-gray-200" />
</a>
</div>

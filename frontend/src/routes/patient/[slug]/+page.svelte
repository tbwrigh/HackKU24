<script lang="ts">
  import type { PageData } from './$types';
  import type { SelectItem } from '$lib/types';
  import Selection from '$lib/selection.svelte';

  export let data: PageData;

  const games = ["Matching", "Flashcards", "Puzzle"];

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

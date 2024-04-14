<script lang="ts">
    import { onMount } from 'svelte';
    import { page } from '$app/stores';

    onMount(() => {
        console.log('Puzzles page mounted');
    });
</script>

<h1>Puzzles {$page.params.slug} - {$page.params.puzzleid}</h1>
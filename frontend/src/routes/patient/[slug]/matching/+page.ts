import type { PageLoad } from './$types';

const backendUrl = import.meta.env.VITE_BACKEND_URL;

export const load: PageLoad = async ({ fetch, params }) => {
  let json: null | JSON = null;
  try {
    const response = await fetch(`${backendUrl}/pair/patient/${params.slug}`);
    json = await response.json();
  } catch (error) {
    console.error('Error:', error);
  }
  return {
    pairs: json
  };
};

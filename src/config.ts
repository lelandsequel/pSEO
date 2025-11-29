// Site configuration based on SITE_ID environment variable

interface SiteConfig {
    theme: string;
    title: string;
    subtitle: string;
    ctaText: string;
    ctaLink: string | null; // null means use dynamic logic
    dataFile: string;
    metaDescription: string;
}

const configs: Record<string, SiteConfig> = {
    layoffs: {
        theme: 'red-600',
        title: 'WarnTracker',
        subtitle: 'Track WARN Notices & Mass Layoffs',
        ctaText: 'Get Resume Help',
        ctaLink: 'https://resume.io',
        dataFile: 'layoffs.json',
        metaDescription: 'Track WARN notices and mass layoffs across companies. Stay informed about workforce reductions and employment changes.',
    },
    errors: {
        theme: 'green-600',
        title: 'RepairHelper',
        subtitle: 'Find Replacement Parts & Fixes Fast',
        ctaText: 'Find Replacement Part',
        ctaLink: null, // Will use dynamic Amazon affiliate link
        dataFile: 'errors.json',
        metaDescription: 'Search thousands of appliance error codes and find replacement parts instantly. Get expert fixes for all major brands.',
    },
};

// Get SITE_ID from environment, default to 'errors'
const siteId = (import.meta.env.SITE_ID || 'errors') as string;

// Export the active configuration
export const config: SiteConfig = configs[siteId] || configs.errors;

// Export helper to check if we're in layoffs mode
export const isLayoffsMode = () => siteId === 'layoffs';
export const isErrorsMode = () => siteId !== 'layoffs';

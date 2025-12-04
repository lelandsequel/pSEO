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
        theme: 'indigo-600',
        title: 'ErrorCodeHelp',
        subtitle: 'OBD2 & System Error Database',
        ctaText: 'Get Best OBD2 Scanner',
        ctaLink: 'https://www.amazon.com/s?k=obd2+scanner&tag=applianceerror-20',
        dataFile: 'layoffs.json',
        metaDescription: 'Comprehensive database of OBD2 and system error codes. Find meanings, causes, and fixes for your check engine light.',
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
    saas: {
        theme: 'purple-900',
        title: 'SaaS Battleground',
        subtitle: 'Unbiased B2B Software Comparisons',
        ctaText: 'Start Free Trial',
        ctaLink: '#',
        dataFile: 'saas.json',
        metaDescription: 'Compare top B2B software tools. In-depth reviews of Project Management, CRM, and Marketing platforms.',
    },
    llc: {
        theme: 'slate-800',
        title: 'StateFiling',
        subtitle: '2025 LLC Filing Costs & Requirements',
        ctaText: 'Start My LLC Now',
        ctaLink: 'https://www.zenbusiness.com',
        dataFile: 'llc.json',
        metaDescription: 'Complete guide to LLC formation costs and requirements for all 50 states. Compare filing fees, processing times, and annual taxes.',
    },
    proposal: {
        theme: 'slate-950',
        title: 'The New Answer',
        subtitle: 'Scaling Infinity Digital Consulting',
        ctaText: 'View Proposal',
        ctaLink: '/proposal',
        dataFile: 'errors.json', // Fallback, not used
        metaDescription: 'Confidential Executive Brief: Programmatic SEO Architecture for Infinity Digital Consulting.',
    },
};

// Get SITE_ID from environment, default to 'errors'
const siteId = (import.meta.env.SITE_ID || 'errors') as string;

// Export the active configuration
export const config: SiteConfig = configs[siteId] || configs.errors;

// Export helper to check if we're in layoffs mode
export const isLayoffsMode = () => siteId === 'layoffs';
export const isErrorsMode = () => siteId !== 'layoffs';

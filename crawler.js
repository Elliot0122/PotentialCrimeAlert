const puppeteer = require('puppeteer');
const fs = require('fs').promises;

(async () => {
  // Read command-line arguments
  const evPage = process.argv[2] || '1'; // Default value is '1' if not provided

  // Initiate the browser
  const browser = await puppeteer.launch({
    headless: 'new'
  });

  // Create a new page in headless Chrome
  const page = await browser.newPage();

  // Go to target website
  await page.goto(`https://www.davisenterprise.com/events/?evPage=${evPage}`, {
    // Wait for content to load
    waitUntil: 'networkidle0'
  });

  // Get full page HTML
  const html = await page.content();

  // Store HTML content in the reactstorefront file with evPage in the filename
  await fs.writeFile(`./data/html/event${evPage}.html`, html);

  // Close headless Chrome
  await browser.close();
})();

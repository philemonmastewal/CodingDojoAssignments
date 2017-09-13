import { FirstComponentPage } from './app.po';

describe('first-component App', () => {
  let page: FirstComponentPage;

  beforeEach(() => {
    page = new FirstComponentPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});

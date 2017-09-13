import { FirstFormPage } from './app.po';

describe('first-form App', () => {
  let page: FirstFormPage;

  beforeEach(() => {
    page = new FirstFormPage();
  });

  it('should display welcome message', () => {
    page.navigateTo();
    expect(page.getParagraphText()).toEqual('Welcome to app!!');
  });
});

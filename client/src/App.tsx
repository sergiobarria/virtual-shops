import * as React from 'react';

import { AppProvider } from '@/src/providers';

export default function App() {
  return (
    <AppProvider>
      <div>Hello World!</div>
    </AppProvider>
  );
}

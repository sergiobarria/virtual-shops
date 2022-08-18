import * as React from 'react';

import { AppProvider } from 'src/providers';
import { AppLayout } from 'src/shared/layouts';
import { AppRoutes } from './routes';

export default function App() {
  return (
    <AppProvider>
      <AppLayout>
        <AppRoutes />
      </AppLayout>
    </AppProvider>
  );
}

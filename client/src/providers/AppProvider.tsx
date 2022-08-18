import * as React from 'react';

import { ThemeProvider } from './theme';
import { QueryProvider } from './query';
import { RouterProvider } from './router';

interface AppProviderProps extends React.PropsWithChildren<{}> {}

export function AppProvider({ children }: AppProviderProps) {
  return (
    <RouterProvider>
      <QueryProvider>
        <ThemeProvider>{children}</ThemeProvider>
      </QueryProvider>
    </RouterProvider>
  );
}

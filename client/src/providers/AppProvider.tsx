import * as React from 'react';

import { ThemeProvider } from './theme';
import { QueryProvider } from './query';

interface AppProviderProps extends React.PropsWithChildren<{}> {}

export function AppProvider({ children }: AppProviderProps) {
  return (
    <QueryProvider>
      <ThemeProvider>{children}</ThemeProvider>
    </QueryProvider>
  );
}

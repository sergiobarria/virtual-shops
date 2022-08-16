import * as React from 'react';
import { MantineProvider } from '@mantine/core';

import { theme } from './theme';

interface ThemeProviderProps {
  children: React.ReactNode;
}

export function ThemeProvider({ children }: ThemeProviderProps) {
  return (
    <MantineProvider
      theme={theme}
      withCSSVariables
      withGlobalStyles
      withNormalizeCSS
    >
      {children}
    </MantineProvider>
  );
}

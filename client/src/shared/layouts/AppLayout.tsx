import * as React from 'react';
import { Box, Sx } from '@mantine/core';

import { AppHeader } from './AppHeader';
import { AppFooter } from './AppFooter';

const appContainerStyles: Sx = {
  display: 'flex',
  flexDirection: 'column',
  minHeight: '100vh',
};

const mainContentStyles: Sx = { flex: 1 };

interface AppLayoutProps extends React.PropsWithChildren<{}> {}

export function AppLayout({ children }: AppLayoutProps) {
  return (
    <Box sx={appContainerStyles}>
      <AppHeader />
      <Box component="main" sx={mainContentStyles}>
        {children}
      </Box>
      <AppFooter />
    </Box>
  );
}

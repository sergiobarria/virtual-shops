import * as React from 'react';
import {
  Box,
  Container,
  Sx,
  Text,
  Center,
  useMantineTheme,
} from '@mantine/core';

const footerStyles: Sx = {
  height: '8rem',
};

const containerStyles: Sx = {
  height: '100%',
  borderTop: '1px solid #f3f3f3',
};

const contentStyles: Sx = {
  height: '100%',
};

export function AppFooter() {
  const theme = useMantineTheme();

  return (
    <Box component="footer" sx={footerStyles}>
      <Container size="lg" sx={containerStyles}>
        <Center sx={contentStyles}>
          <Text size="sm" color={theme.colors.gray[6]}>
            &copy; Copyright Virtual Shops - {new Date().getFullYear()}
          </Text>
        </Center>
      </Container>
    </Box>
  );
}

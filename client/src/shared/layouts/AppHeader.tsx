import * as React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import {
  Box,
  Container,
  Group,
  MantineTheme,
  Sx,
  Image,
  Anchor,
} from '@mantine/core';
import { IconShoppingCart, IconUser } from '@tabler/icons';

import { LOGO_SVG } from 'src/shared/assets';
import * as appRoutes from 'src/shared/constants/routes';

const navLinks = [
  {
    id: 1,
    label: 'cart',
    to: appRoutes.cart,
    icon: <IconShoppingCart size={20} />,
  },
  {
    id: 2,
    label: 'sign in',
    to: appRoutes.signIn,
    icon: <IconUser size={20} />,
  },
];

const headerStyles: Sx = (theme: MantineTheme) => ({
  backgroundColor: theme.colors.dark[7],
  color: 'white',
});

const headerContainerStyles: Sx = {
  height: '5rem',
  '& > *': {
    height: '100%',
  },
};

const navLinkStyles: Sx = (theme: MantineTheme) => ({
  textTransform: 'uppercase',
  color: theme.colors.gray[5],
  fontWeight: 500,
  fontSize: theme.fontSizes.sm,
  transition: 'all 300ms ease-in-out',
  padding: '0.5rem 1rem',
  '&:hover': {
    textDecoration: 'none',
    color: theme.colors.gray[3],
    backgroundColor: theme.colors.gray[8],
  },
});

export function AppHeader() {
  return (
    <Box component="header" sx={headerStyles}>
      <Container size="lg" sx={headerContainerStyles}>
        <Group position="apart">
          <Box>
            <Anchor component={RouterLink} to={appRoutes.home}>
              <Image src={LOGO_SVG} width={150} alt="app logo" />
            </Anchor>
          </Box>

          {/* Nav Links */}
          <Group spacing={30}>
            {navLinks.map(({ id, to, icon, label }) => (
              <Anchor
                key={id}
                component={RouterLink}
                to={to}
                sx={navLinkStyles}
              >
                <Group spacing={5} align="center">
                  {icon}
                  {label}
                </Group>
              </Anchor>
            ))}
          </Group>
        </Group>
      </Container>
    </Box>
  );
}

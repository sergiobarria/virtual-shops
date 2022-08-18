import * as React from 'react';
import { Routes, Route } from 'react-router-dom';

import { HomePage } from 'src/pages';
import * as appRoutes from 'src/shared/constants/routes';

export function AppRoutes() {
  return (
    <React.Fragment>
      <Routes>
        <Route path={appRoutes.home} element={<HomePage />} />
      </Routes>
    </React.Fragment>
  );
}

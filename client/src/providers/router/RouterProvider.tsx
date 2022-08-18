import * as React from 'react';
import { BrowserRouter } from 'react-router-dom';

interface RouterProviderProps extends React.PropsWithChildren<{}> {}

export function RouterProvider({ children }: RouterProviderProps) {
  return <BrowserRouter>{children}</BrowserRouter>;
}

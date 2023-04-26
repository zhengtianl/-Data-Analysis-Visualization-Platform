import { Route, Routes } from 'react-router-dom';
import CoverPages from "@/pages/CoverPages"
import { unstable_HistoryRouter as HistoryRouter } from 'react-router-dom';

function App() {
  return (
      <div className="App">
          <CoverPages></CoverPages>
      </div>
  );
}

export default App;

import { createContext, useState, useEffect } from "react";

export const AuthContext = createContext();

const getInitialState = () => {
  const user = sessionStorage.getItem("user");
  return user ? JSON.parse(user) : null;
};

export const AuthProvider = ({ children }) => {
  //const [user, setUser] = useState([]);
  const [user, setUser] = useState(getInitialState);

  useEffect(() => {
    sessionStorage.setItem("user", JSON.stringify(user));
  }, [user]);

  const authlogin = (
    email,
    password,
    idclinica,
    idusuario,
    idperfil,
    clinica
  ) => {
    setUser({
      email: email,
      password: password,
      idclinica: idclinica,
      idusuario: idusuario,
      idperfil: idperfil,
      clinica: clinica,
    });
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        authlogin,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

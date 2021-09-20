
let huitreines =
  let placements = Array.make 8 1000 in
  let rec placer ligne =
    if ligne<8 then
    
      begin
      for col=0 to 7 do
        let possible = ref true in
        for k=0 to (ligne-1) do
          begin
          if (placements.(k)= col || 
            (placements.(k)+k) = (col+ligne) ||
          (placements.(k)-k) = (col-ligne)) then
            possible:= false;
          if !possible then
            (placements.(ligne)<-col;
            placer (ligne+1))
            end
            done;
        done;
      end in
      placer 0;placements;;
let t = huitreines;;
